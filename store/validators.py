from django.core.exceptions import ValidationError

def validate_file_size(file):
    max_size_kb = 500 # for testing purpose
    
    if file.size > max_size_kb * 1024:
        raise ValidationError(f'files cannot be larger than {max_size_kb}KB!')
    