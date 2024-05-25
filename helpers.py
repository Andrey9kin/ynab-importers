import os

def find_files(args, prefix, suffix):
    result = []
    if len(args) > 1:
        for file_path in args[1:]:
            if os.path.isfile(file_path):
                result.append(file_path)
            else:
                print(f'File {file_path} does not exist')
    else:
        # Search for files that start from prefix and end with suffix
        for file_path in os.listdir():
            if file_path.startswith(prefix) and file_path.endswith(suffix):
                result.append(file_path)
    print('Found the following transaction files: {}'.format(result))
    
    return result