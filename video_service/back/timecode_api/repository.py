from .services.data_mining import Collector


# think of it as validated data from a repository/database
try:
    data = Collector("../../files")
    data.scann_folder_with_data()
except:
    data = Collector("./files")
    data.scann_folder_with_data()
