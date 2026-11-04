# -*- coding: utf-8 -*-
"""
转录：原始 m4a -> 带时间戳文本 + 纯文本
输出到 raw/notes/video-transcripts/
模型: faster-whisper large-v3 (中文, 保守 VAD 避免切碎句子)

【关键实测结论 2026-07-09】不要对录音做神经降噪前置！
A/B 测试证明：dns64 神经降噪 + loudnorm 会损伤语音，导致关键实体丢失
(如"来天美的成都"→"我来感受"、"在腾讯"→"在工作的一些职业群")。
whisper large-v3 训练时已见过噪声，能自行处理背景噪声；
神经降噪引入的失真比噪声更伤转写。原始直转质量最佳。
详见 log.md 2026-07-09 条目与 raw/m4a/AGENTS.md。
"""
import os, glob, time, sys, warnings, json
warnings.filterwarnings("ignore")
os.environ.setdefault("PYTHONUNBUFFERED","1")

IN_GLOB = "*.m4a"
OUT_DIR = "../notes/video-transcripts"

def fmt(s): h=int(s//3600);m=int((s%3600)//60);s=int(s%60);return f"{h:02d}:{m:02d}:{s:02d}"

def main(files=None):
    from faster_whisper import WhisperModel
    print("loading large-v3 ...", flush=True)
    model = WhisperModel("large-v3", device="cuda", compute_type="float16")
    print("model ready", flush=True)
    if files is None:
        files = sorted(glob.glob(IN_GLOB))
    print(f"待转录(原始m4a): {len(files)} 个 -> {OUT_DIR}/", flush=True)
    os.makedirs(OUT_DIR, exist_ok=True)
    summary=[]
    for fpath in files:
        base = os.path.splitext(os.path.basename(fpath))[0]
        out_ts = os.path.join(OUT_DIR, f"{base}.transcript.txt")
        out_full = os.path.join(OUT_DIR, f"{base}.full.txt")
        # 强制覆盖（复原版是错的）
        print(f"\n=== {os.path.basename(fpath)} ===", flush=True)
        t0=time.time()
        segments, info = model.transcribe(
            fpath, language="zh", beam_size=5,
            vad_filter=True,
            vad_parameters=dict(min_silence_duration_ms=2000, speech_pad_ms=200, threshold=0.5),
            condition_on_previous_text=True,
        )
        print(f"  lang={info.language}({info.language_probability:.2f}) dur={fmt(info.duration)}", flush=True)
        lines_ts, lines_full = [], []
        for seg in segments:
            lines_ts.append(f"[{fmt(seg.start)}-{fmt(seg.end)}] {seg.text.strip()}")
            lines_full.append(seg.text.strip())
            if len(lines_ts) % 120 == 0:
                print(f"    ...{fmt(seg.end)} ({len(lines_ts)} segs)", flush=True)
        with open(out_ts,"w",encoding="utf-8") as f:
            f.write(f"# 转录(原始m4a直转) | {base}\n# 语言={info.language} 时长={fmt(info.duration)} 模型=large-v3 VAD=保守(2s)\n\n")
            f.write("\n".join(lines_ts))
        with open(out_full,"w",encoding="utf-8") as f:
            f.write("\n".join(lines_full))
        dt=time.time()-t0
        print(f"  完成: {len(lines_ts)}段 耗时{dt:.0f}s ({info.duration/dt:.1f}x)", flush=True)
        summary.append({"file":base,"segs":len(lines_ts),"dur_s":round(info.duration),"time_s":round(dt)})
    with open("_transcribe_summary.json","w",encoding="utf-8") as f:
        json.dump(summary,f,ensure_ascii=False,indent=2)
    print("\n=== 汇总 ===")
    for s in summary: print(f"  {s['file']}: {s['segs']}段 {fmt(s['dur_s'])} 耗时{s['time_s']}s")
    print("全部完成。")

if __name__ == "__main__":
    # 默认转文件1验证；传 "all" 转全部
    if len(sys.argv) > 1 and sys.argv[1] == "all":
        main()
    elif len(sys.argv) > 1:
        main(sys.argv[1:])
    else:
        main(["2025年11月10日 14点33分(2).m4a"])
