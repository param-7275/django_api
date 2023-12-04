from django.core.exceptions import ValidationError


def validate_file_extension(value):
    allowed_extensions = ['pptx', 'docx', 'xlsx']
    extension = value.name.split('.')[-1].lower()

    if extension not in allowed_extensions:
        raise ValidationError('File type not supported. Allowed types: pptx, docx, xlsx')