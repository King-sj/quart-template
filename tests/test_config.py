def test_pytest_ini_read(pytestconfig):
  '''
  测试读取 pytest.ini 文件
  '''
  assert pytestconfig.getini('testpaths') == ['tests']
