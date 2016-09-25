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

That may not be particularly exciting in-and-of itself, but future versions  plan to add jinja templating, scriptingm for populating directories, and more.
