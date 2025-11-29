import pytest
from Calculator.calculator import add, subtract, divide, multiply,main

#Test Addition
def test_add():
    assert add(2,3) == 5
    assert add(19,8) == 27
    assert add(0,3) == 3

#Test Subtraction
def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(30, 20) == 10
    assert subtract(22, 6) == 16

#Test Multiplication
def test_multiply():
    assert multiply(3, 3) == 9
    assert multiply(5, 6) == 30
    assert multiply(6, 6) == 36

#Test Divison
def test_divide():
    assert divide(10, 2) == 5
    assert divide(40, 10) == 4
    assert divide(10, 10) == 1

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)

#test user input and addition
def test_Cli_Addition(monkeypatch,capsys):
    inputs = iter(["1","2","3","0"])
    monkeypatch.setattr("builtins.input", lambda: next(inputs))
    main()

    out = capsys.readouterr().out

    assert "Result: 5" in out
    assert "Goodbye" in out

#test user input and subtraction
def test_Cli_Subtraction(monkeypatch,capsys):
    inputs = iter(["2","5","3","0"])
    monkeypatch.setattr("builtins.input", lambda: next(inputs))
    main()

    out = capsys.readouterr().out

    assert "Result: 2" in out
    assert "Goodbye" in out

#test user input and Multiplication
def test_Cli_Multiplication(monkeypatch,capsys):
    inputs = iter(["3","3","3","0"])
    monkeypatch.setattr("builtins.input", lambda: next(inputs))
    main()

    out = capsys.readouterr().out

    assert "Result: 9" in out
    assert "Goodbye" in out

#test user input and Divison
def test_Cli_Divison(monkeypatch,capsys):
    inputs = iter(["4","10","2","0"])
    monkeypatch.setattr("builtins.input", lambda: next(inputs))
    main()

    out = capsys.readouterr().out

    assert "Result: 5" in out
    assert "Goodbye" in out

