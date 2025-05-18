from {{cookiecutter.project_slug}}.main import hello_world

def test_main(capsys):
    hello_world()
    captured = capsys.readouterr()
    assert "Hello World!" in captured.out
