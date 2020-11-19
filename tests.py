from IPython.display import display, Markdown
import math
import json
import pickle
import os

answer_path = os.path.join('data','dictionary.json')

with open(answer_path, 'r') as fp:
    answer = json.load(fp)
    
class CheckDictionary():
    def __init__(self, dictionary):
        self.data = {}
        self.dictionary = dictionary
        
        for key in self.dictionary.keys():
            try:
                if math.isnan(self.dictionary[key]['stats']['type2']):
                    self.dictionary[key]['stats']['type2'] = 'None'
            except:
                continue

    def check_keys(self):
        keys = list(self.dictionary.keys())
        if all([x in ['Bayleef', 'Haunter', 'Poliwag', 'Pidgeotto', 'Kadabra'] for x in keys]):
            self.data['keys'] = 1
        else:
            self.data['keys'] = 0
        
    def check_values(self):
        nan = float('nan')
        self.answer = answer

        if list(self.dictionary.values()) == list(answer.values()):
            self.data['values'] = 1
        else:
            self.data['values'] = 0
            
    def results(self):
        check = '✅'
        X = '❌'
        correct = sum(self.data.values())
        
        if correct == len(self.data):
            header_emoji = check
        else:
            header_emoji = X
            
        
        header = '''# {} Your dictionary passed {} out of {} tests!\n\n'''.format(header_emoji, correct, len(self.data))
        
        
        

        if self.data['keys'] == 1:
            md = '''>{} *Dictionary Keys are correct!*'''.format(check)
            
        else:
            md = '''>{} *Dictionary Keys are incorrect*'''.format(X)
            
        md += "\n\n"    
        if self.data['values'] == 1:
            md += '''>{} *Dictionary data are correct!*'''.format(check)
        else:
            md += '''>{} *Dictionary data are incorrect.*'''.format(X)
            
        block = Markdown(header + md)
        
        display(block)
        
        
    def run(self):
        self.check_keys()
        self.check_values()
        self.results()
        
list_path = os.path.join('data', 'list.txt')       
with open(list_path, "rb") as fp:   # Unpickling
    list_test = pickle.load(fp)

class ListCheck():
    def __init__(self, list_):
        self.list = list_
        self.data = {}
        
    def check_length(self):
        if len(list_test) == len(self.list):
            self.data['length'] = 1
        else:
            self.data['length'] = 0
            
    def compare_lists(self):
        A = set(list_test)
        B = set(self.list)
        self.missing = A - B
        self.wrong = B - A
        
        if len(self.missing) == 0:
            if len(self.wrong) == 0:
                self.data['data'] = 1
            else:
                self.data['data'] = 0
        else:
                self.data['data'] = 0
                
        
        self.data['missing'] = self.missing
        self.data['wrong'] = self.wrong
        
    def results(self):
        check = '✅'
        X = '❌'
        if self.data['length'] == 1:
            md = '''>{} *List length is correct!*'''.format(check)
        else:
            md = '''>{} *List length is incorrect*'''.format(X)
            
        if len(self.data['missing']) > 0:
            number = len(self.data['missing'])
            md += '''\n\n>{} *List is missing {} data points* \n\n<details><summary>Click here to view what is missing.</summary>'''.format(X, number)
        
            for data in self.data['missing']:
                md += '''\n\n- {}'''.format(data)
                
            md += '</details>'
            
        if len(self.data['wrong']) > 0:
            number = len(self.data['wrong'])
            if number > 1:
                point = 'points'
            else:
                point = 'point'
            md += '''\n\n>{} *List contains {} incorrect data {}*\n\n\n\n<details><summary>Click here to view what data points are wrong</summary>'''.format(X, number, point)
            
            for data in self.data['wrong']:
                md +='''\n\n- {}'''.format(data)
                
            md += '</details>'
        else:
            md +='''\n\n>{} *List data are correct*'''.format(check)
            
        correct = self.data['length'] + self.data['data']
        md = '# Your list passed {} out of {} tests!\n\n'.format(correct, 2) + md
            
        md = Markdown(md)
        display(md)
        
            
    def run(self):
        self.check_length()
        self.compare_lists()
        self.results()
        
        
class VariableAssignment:
    
        def run(self, pokemon_count, trainer_level,
                coolest_pokemon, favorite_pokemon, 
                hours_per_day, joels_pokemon_names):
            assert type(pokemon_count) == int, '❌ pokemon_count has the wrong datatype.'
            assert type(trainer_level) == str, '❌ trainer_level has the wrong datatype.'
            assert type(coolest_pokemon) == str, '❌ coolest_pokemon has the wrong datatype.'
            assert type(favorite_pokemon) == str, '❌ favorite_pokemon has the wrong datatype.'
            assert type(hours_per_day) == float, '❌ hours_per_day has the wrong datatype.'
            assert type(joels_pokemon_names) == list, 'joels_pokemon_names has the wrong datatype.'

            assert pokemon_count == 5, '❌ pokemon_count was set to the wrong number.'
            assert trainer_level.strip().lower() == 'apprentice', '❌ trainer_level has the wrong value.'
            assert trainer_level == 'Apprentice', '❌ trainer_level is formatted incorrectly.'
            assert coolest_pokemon.strip().lower() == 'haunter', '❌ coolest_pokemon has the wrong value.'
            assert coolest_pokemon == 'Haunter', '❌ coolest_pokemon is formatted incorrectly.'
            assert favorite_pokemon.strip().lower() == 'kadabra', '❌ favorite_pokemon has the wrong value.'
            assert favorite_pokemon == 'Kadabra', '❌ favorite_pokemon is formatted incorrectly.'
            assert joels_pokemon_names == ['Bayleef', 'Haunter', 'Poliwag', 'Pidgeotto', 'Kadabra'], '❌ joels_pokemon_names has the wrong values.'
            
            print('✅ All tests were passed!')
        

class PokemonWithType:
    
    def solution(self, pokemon_type, data):

        pokemon_names = set()
        for key in data.keys():
            if data[key]['stats']['type1'] == pokemon_type:
                pokemon_names.add(key)
            elif data[key]['stats']['type2'] == pokemon_type:
                pokemon_names.add(key)

        pokemon_names = list(pokemon_names)
        return pokemon_names
    
    def run(self, answer, data):
        
        assert answer('grass') == self.solution('grass', data)
        assert answer('ghost') == self.solution('ghost', data)
        assert answer('rock') == self.solution('rock', data)
        assert answer('steel') == self.solution('steel', data)
        print('✅ All tests were passed!')
        
        
class StatByType:
    
    def solution(self, stat, pokemon_type, data):
        
        pokemon_names = self.pokemon_with_type(pokemon_type)
        stats = [data[name]['stats'][stat] for name in pokemon_names]
        return stats
    
    def pokemon_with_type(self, pokemon_type):
        data = self.data
        pokemon_names = set()
        for key in data.keys():
            if data[key]['stats']['type1'] == pokemon_type:
                pokemon_names.add(key)
            elif data[key]['stats']['type2'] == pokemon_type:
                pokemon_names.add(key)

        pokemon_names = list(pokemon_names)
        return pokemon_names

    
    def run(self, answer, data):
        self.data = data
        assert answer('attack', 'grass') == self.solution('attack', 'grass', data)
        assert answer('defense', 'ghost') == self.solution('defense','ghost', data)
        assert answer('hp','rock') == self.solution('hp','rock', data)
        assert answer('speed','steel') == self.solution('speed','steel', data)
        print('✅ All tests were passed!')
        
            