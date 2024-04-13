# �������� ������� ������ get ��� �������.
# ������ ������ ������� ������� ��������� ���� � �������� �� ���������.
# ��� ��������� � ��������������� ����� ������� ������ ���������� ��������� ��������.
# ���������� ������ ����� ��������� ����������

def get(dictionary,key,default=None):
    try:
        return dictionary[key]
    except KeyError:
        return default

data_dict = {1:'one', 2:'two'}
key = 1
data_dict = get(data_dict,key)
print(f' �������� ��� �����"{key}":{data_dict}')

