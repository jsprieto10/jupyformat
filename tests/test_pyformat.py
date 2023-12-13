from pyformat import reads


def test_reads():

    result = reads("output = '# Title'")
    print(result)
