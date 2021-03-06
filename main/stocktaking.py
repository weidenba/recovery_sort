from helper.meta import generate_uid, get_file_size, get_file_name, get_modification_date, get_file_mime


def get_file_meta(file_path):
    file_meta = {
        'path': file_path,
        'name': get_file_name(file_path),
        'uid': generate_uid(file_path),
        'mod_date': get_modification_date(file_path),
        'mime': get_file_mime(file_path),
        'size': get_file_size(file_path)
    }
    return file_meta
