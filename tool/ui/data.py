import glob

def get_files():
    hard_coded_path = "C:/Users/ray55/OneDrive/Documents/MOVIE/ASSETS/CAR"
    files = glob.glob(hard_coded_path + "/**/**/*.mb")
    return files

if __name__ == '__main__':
    for f in get_files():
        print(f)
