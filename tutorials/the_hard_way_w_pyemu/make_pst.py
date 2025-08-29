import pyemu
iofiles = pyemu.helpers.parse_dir_for_io_files(".")
pst = pyemu.Pst.from_io_files(*iofiles)
pst.model_command = "mf6"
pst.control_data.noptmax = 0
pst.write("pest.pst")