from cx_Freeze import setup, Executable

setup(
    name = "gui",
    version = "1.0",
    description = "EvaluatesChemicalClassifications.",
    executables = [Executable("gui.py")]
)