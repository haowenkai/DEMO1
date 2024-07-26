#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    """
    主函数：运行管理任务。

    此函数初始化Django环境并执行命令行指令。
    """
    # 设置DJANGO_SETTINGS_MODULE环境变量的默认值
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DEMO1.settings')

    try:
        # 尝试从django.core.management导入execute_from_command_line函数
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # 如果无法导入Django，抛出ImportError，并提供问题排查指导
        raise ImportError(
            "未能导入Django。请确认是否已安装并在PYTHONPATH环境变量中可用？是否忘记激活虚拟环境？"
        ) from exc
    # 执行通过sys.argv传入的命令行指令
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
