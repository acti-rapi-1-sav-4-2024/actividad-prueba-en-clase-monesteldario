def func(x):
    return x + 5
#prueba dario

def test_answer():
    # arrange
    result = 0
    # act
    result = func(3)
    # assert
    assert result == 5, f"El número esperado es 5, pero su función devuelve: {result}"
