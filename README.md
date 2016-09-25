# Dirge
Dirge - Directory generator

Dirge can generate a directory structure from a template file. For example:

```
root
  |
  +-s1_1
  |
  +-s1_2
  |  |
  |  `-s2_1
  |
  `-s1_3
```

Generates directories with the following paths:

```
root
root/s1_1
root/s1_2
root/s1_2/s2_1
root/s1_3
```

Directory description files can be fairly flexible, using almost any sane representation of a directory tree. For example, the following file, which was generated from the output of the `tree` command on a directory tree:

```
top
 ├─first
 │  └─second
 ├─third
 └─fourth
```

Generates:

```
top
top\first
top\first\second
top\fourth
top\third
```

The benefit being that you can create actual directory trees on the filesystem, get the information from `tree` and create a file that dirge can use to copy the exact structure anywhere else. Additionally, though the previous two examples show a tree from a single root, dirge can handle multiple top-level directories, or just a flat list of directories:

```
aaa
bbb
 +-sub-bbb
   +-sub-sub-bbb
ccc
ddd
 +-sub-ddd
eee
```

Generates:

```
aaa
bbb
bbb\sub-bbb
bbb\sub-bbb\sub-sub-bbb
ccc
ddd
ddd\sub-ddd
eee
```

That may not be particularly exciting in-and-of itself, but future versions plan to add jinja templating, scripting for populating directories, and more.
