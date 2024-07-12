from cx_Freeze import setup, Executable

# Specify the full path to your icon file
icon_path = r"C:\Users\ASUS\Desktop\IPS Energy\Project1\myicon.ico"

# Define the executable
target = Executable(
    script="solar_inverter_selector.py",
    base="Win32GUI",
    icon=icon_path
)

# Setup configuration
setup(
    name="Solar Inverter Selector",
    version="1.0",
    description="A tool to select suitable solar inverters",
    options={"build_exe": {"include_files": [icon_path]}},  # Ensure icon file is included
    executables=[target]
)
