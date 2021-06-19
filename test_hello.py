def test_test2(capsys):	
	import hello 
	stdout, stderr = capsys.readouterr()
	assert stdout == 'Hello world from dev\n'
	
	
