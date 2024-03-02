import subprocess
import pytest

INTERPRETER = 'python'

def run_script(filename, input_data=None):
    proc = subprocess.run(
        [INTERPRETER, filename],
        input='\n'.join(input_data if input_data else []),
        capture_output=True,
        text=True,
        check=False
    )
    return proc.stdout.strip()

test_data = {
    'python_if_else': [
        ('1', 'Weird'),
        ('4', 'Not Weird'),
        ('3', 'Weird'),
        ('6','Weird'),
        ('22', 'Not Weird')
    ],
    'arithmetic_operators': [
        (['1', '2'], ['3', '-1', '2']),
        (['10', '5'], ['15', '5', '50']),
        (['20', '30'], ['50', '-10', '600'])
    ],
    'division': [
        (['7','2'],['3','3.5']),
        (['4','10'],['0','0.4']),
        (['100','0'],['0'])
    ],
    'loops': [
        (['11'],['0','1','4','9','16','25','36','49','64','81','100']),
        (['4'],['0','1','4','9']),
        (['8'],['0','1','4','9','16','25','36','49'])
    ],
    'print_function': [
        (['5'],['12345']),
        (['10'],['12345678910']),
        (['30'],['ERROR'])
        ],
    'second_score': [
        (['5','1 2 3 4 5 5'],['4']),
        (['8','1 1 1 1 3 3 5 6'],['5']),
        (['6','22 33 44 44 99 11'],['44'])
    ],
    'nested_list': [
       (['3','Arnold','40','Bob','30','Suzi','20'],['Bob']),
       (['4','Arnold','100','Dima','77','Bob','77','Suzi','50'],['Bob','Dima']),
    ],
    'lists': [    
       (['4','insert 0 2','append 1','pop','print'],['[2]']),
       (['6','insert 0 1','insert 0 2','append 3','insert 4 4','sort','print'],['[1, 2, 3, 4]']),
       (['6','append 1','append 2','append 3','remove 3','reverse','print'],['[2, 1]'])
    ],
    'swap_case': [
        (['hockey'],['HOCKEY']),
        (['FOOTBALL'],['football']),
        (['VoLLeyBaLL'],['vOllEYbAll'])
    ],
    'split_and_join': [
        (['OO OO OO'],['OO-OO-OO']),
        (['One person'],['One-person']),
        (['1 2 3 4 5 6'],['1-2-3-4-5-6']),
    ],
    'anagram': [
       (['ramnaga','anagram'],['YES']),
       (['APEX','PXAE'],['YES']),
       (['BALL','FOOTBALL'],['NO']),
    ],
    'metro': [
        (['3','10 20','20 34','15 20','20'],['3']),
        (['1','17 20','17'],['1']),
        (['2','14 18','14 20','14'],['2'])

    ],
    'minion_game': [
       (['BANANA'],['Stuart 12']),
       (['CHOCOLATE'],['Stuart 29']),
       (['ALIEN'],['Kevin 10'])
    ],
     'is_leap': [
       (['2024'],['True']),
       (['1900'],['False']),
       (['2150'],['False']),
       (['2324'],['True']),
       (['3333'],['False']),
       (['112024'],['True']),
   ],
   'happiness': [
       (['3 3','1 2 3','3 2 1','4 5 6'],['3']),
       (['4 6','1 2 3 4','5 6 7 8','8 7 6 5'],['0']),
       (['2 2','1 2','6 7','2 1'],['-2']),
       (['3 3','33 44 55','34 45 55','35 46 56'],['1'])
   ],
   'pirate_ship': [
       (['50 3','1 25 500','2 25 400','3 50 300'],['1 25.00 500.00','2 25.00 400.00']),
        (['100 4','груз1 66 1000','груз2 30 5000','груз3 10 10000','груз4 1 100000'],['груз4 1.00 100000.00','груз3 10.00 10000.00','груз2 30.00 5000.00','груз1 59.00 893.94']),
        (['50 3','груз1 28 1345','груз2 31 2790','груз3 14 3320'],['груз3 14.00 3320.00','груз2 31.00 2790.00','груз1 5.00 240.18']),
        (['100 3','1 87 1000','2 62 1010','3 45 990'],['3 45.00 990.00','2 55.00 895.97'])
   ],
   'matrix_mult': [
       (['2','2 2','3 3','2 2','3 3'],['10 10','15 15']),
       (['4','1 2 3 4','4 3 2 1','1 2 3 4','4 3 2 1','1 1 1 1','2 2 2 2','3 3 3 3','4 4 4 4'],['30 30 30 30','20 20 20 20','30 30 30 30','20 20 20 20']),
       (['2','11 11','11 11','22 22','22 22'],['484 484','484 484'])
   ]
}

def test_hello_world():
    assert run_script('hello_world.py') == 'Hello, World!'

@pytest.mark.parametrize("input_data, expected", test_data['python_if_else'])
def test_python_if_else(input_data, expected):
    assert run_script('python_if_else.py', [input_data]) == expected

@pytest.mark.parametrize("input_data, expected", test_data['arithmetic_operators'])
def test_arithmetic_operators(input_data, expected):
    assert run_script('arithmetic_operators.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['division'])  
def test_division(input_data, expected):
    assert run_script('division.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['loops']) 
def test_loops(input_data, expected):
    assert run_script('loops.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['print_function']) 
def test_print_function(input_data, expected):
    assert run_script('print_function.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['second_score']) 
def test_second_score(input_data, expected):
    assert run_script('second_score.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['nested_list']) 
def test_nested_list(input_data, expected):
    assert run_script('nested_list.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['lists']) 
def test_lists(input_data, expected):
    assert run_script('lists.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['swap_case']) 
def test_swap_case(input_data, expected):
    assert run_script('swap_case.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['split_and_join']) 
def test_split_and_join(input_data, expected):
    assert run_script('split_and_join.py', input_data).split('\n') == expected

def test_max():
    assert run_script('max_word.py') == 'сосредоточенности'

def test_price_sum():
    assert run_script('price_sum.py') == '6842.84 5891.06 6810.90'


@pytest.mark.parametrize("input_data, expected", test_data['split_and_join']) 
def test_split_and_join(input_data, expected):
    assert run_script('split_and_join.py', input_data).split('\n') == expected


@pytest.mark.parametrize("input_data, expected", test_data['anagram']) 
def test_anagram(input_data, expected):
    assert run_script('anagram.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['metro']) 
def test_metro(input_data, expected):
    assert run_script('metro.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['minion_game']) 
def test_minion_game(input_data, expected):
    assert run_script('minion_game.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['is_leap']) 
def test_is_leap(input_data, expected):
    assert run_script('is_leap.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['happiness']) 
def test_happiness(input_data, expected):
    assert run_script('happiness.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['pirate_ship']) 
def test_pirate_ship(input_data, expected):
    assert run_script('pirate_ship.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['matrix_mult']) 
def test_matrix_mult(input_data, expected):
    assert run_script('matrix_mult.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['minion_game']) 
def test_minion_game(input_data, expected):
    assert run_script('minion_game.py', input_data).split('\n') == expected