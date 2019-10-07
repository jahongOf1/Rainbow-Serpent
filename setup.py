import cx_Freeze

executables = [cx_Freeze.Executable("rainbow_serpent.py")]

cx_Freeze.setup(
	name= "Rainbow Serpent",
	options={"build_exe":{"packages": ["pygame"], 
		"include_files":["redball.png", "blueball.png", "greenball.png"]}},
	executables = executables
	)