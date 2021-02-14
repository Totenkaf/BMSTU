def filePreparation(filename):
    names = ["Addr", "Command", "Pressure", "Time", "Date"]
    sensor_surf = pd.read_csv(filename, skiprows = 2, header=None, delimiter=';', names=names)
