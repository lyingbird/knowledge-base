# -*- coding: utf-8 -*-
"""
句子合并后处理：把 whisper 的碎片段合并成可读整句。
输入: {base}.transcript.txt (带时间戳碎片段)
输出: {base}.readable.txt (合并后的可读版本，仍带时间戳)
不动原始 .transcript.txt。

合并策略：
- 累积文本，遇句末标点(。？！.?!)或累积>=30字则断句
- 时间戳取合并段的首段时间
- 最大长度50字(防止过长难读)
"""
import os, re, glob

def parse_line(line):
    m = re.match(r'^\[([\d:]+)-([\d:]+)\]\s*(.*)$', line)
    if not m: return None
    return (m.group(1), m.group(2), m.group(3).strip())

def merge_file(path):
    out = os.path.splitext(path)[0] + ".readable.txt"
    if os.path.exists(out):
        print(f"[skip] {os.path.basename(out)} 已存在"); return
    with open(path, encoding="utf-8") as f:
        lines = [parse_line(l) for l in f if l.startswith("[")]
    lines = [l for l in lines if l]
    merged = []
    buf_start = buf_end = None
    buf = ""
    for st, en, t in lines:
        if buf_start is None:
            buf_start = st; buf_end = en
        buf += t
        buf_end = en
        # 断句条件：句末标点 或 累积>=30字 或 已达50字强制断
        if re.search(r'[。？！.?!；;]$', buf) or len(buf) >= 30 or len(buf) >= 50:
            merged.append((buf_start, buf_end, buf.strip()))
            buf = ""; buf_start = None
    if buf:
        merged.append((buf_start, buf_end, buf.strip()))
    with open(out, "w", encoding="utf-8") as f:
        f.write(f"# 可读版(句子合并) | {os.path.basename(path)}\n# 原始 {len(lines)} 段 -> 合并 {len(merged)} 句\n\n")
        for st, en, t in merged:
            f.write(f"[{st}] {t}\n")
    print(f"  {os.path.basename(path)}: {len(lines)}段 -> {len(merged)}句 -> {os.path.basename(out)}")

def main():
    files = sorted(glob.glob("2025年11月10日*.transcript.txt") +
                   glob.glob("2026年01月23日*.transcript.txt"))
    print(f"待合并: {len(files)} 个文件")
    for f in files:
        merge_file(f)
    print("完成。")

if __name__ == "__main__":
    main()
