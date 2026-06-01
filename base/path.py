from pathlib import Path

print(Path.cwd())

base = Path.cwd()
data_path = base / 'meta_class.md'
print(data_path)

# .name：完整文件名（带后缀）
print(data_path.name)
# .stem：去掉后缀的「主干」
print(data_path.stem)
# .suffix：扩展名（带点）
print(data_path.suffix)
# .parent：父目录
print(data_path.parent)

# .iterdir()：只列当前目录下一层
# .glob(pattern)：匹配模式（仅当前目录）
# .rglob(pattern)：递归匹配
md_files = list(Path.cwd().rglob('*.md'))
print(f'找到 {len(md_files)} 个 markdown 文件')


content = data_path.read_text(encoding='utf-8')
# print(content)#
# p.write_text('两点水的打卡记录\n', encoding='utf-8')



# with data_path.open('r', encoding='utf-8') as f:
#     for line in f:
#         print(line.rstrip())


# .mkdir() 创建目录
# .touch() 创建空文件
# .unlink() 删除文件
# shutil.rmtree(p) 删除目录

# 改个名字：with_name / with_stem / with_suffix