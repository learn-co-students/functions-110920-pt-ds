# –– Functions ––

![Pokeball](https://media.giphy.com/media/R9zXHWAHyTjnq/giphy.gif)

### Question:

Why do we use functions?

YOUR ANSWER HERE

### Create a basic function

<u>In the cell below:</u>

Write a function called `hello` that receives a name and does the following:
1. prints the string "Hello \<name>" 
2. returns the string "\<name> said Hello!"



**In the cell below,** we import the Pokemon Dataset.

*Don't worry about this code for now. Just run the cell ☺️*

### Previous Lesson:

![](https://gamepress.gg/pokemonmasters/sites/pokemonmasters/files/styles/300h/public/2019-08/pm0153_00_bayleaf_256.ktx.png?itok=Tr7OMsm1)

**Bayleef** is Joél's strongest pokemon. Let's create a list of all Pokemon that Bayleef is weak against.

Our dictionary gives us the *Types* of pokemon Bayleef is weak to. Our dictionary also gives us the type for each pokemon. So first we have to figure out what types of pokemon Bayleef is weak to, then grab every pokemon that has that type.

**Ok, here is how we will do it.**

*Weakness* is measured with the ```weakness``` key in our data. If the weakness value = 2, that means the pokemon is extremely weak to that type of pokemon. 

To find all pokemon that Bayleef is weak to, we have to:
1. Isolate Bayleef's weakness data from our dictionary
2. Identify any type that has a weakness score of 2 and append those types to a list called ```weakness_types```
3. Loop over our entire dataset
4. Identify pokemon who have a type that match the types in our ```weakness_types``` list.
> **Hint** The type of each pokemon can be found using the ```stats``` key
5. Append the names of those pokemon to a list called ```bayleef_weakness```

-----------------

**Let's walk through steps 1 and 2.**

You will code steps 3-5!

**Step 1:** Isolate Bayleef's weakness data from our dictionary

**Step 2:** Identify any type that has a weakness score of 2 and appending those types to a list called ```weakness_types```


We do this by:
1. Creating an empty list
2. Looping over the keys of our newly made dictionary```bayleef_weakness_score```.
    - Each key is a pokemon type
3. Checking if the score equals 2
4. Appending the key to our empty list if the score equals 2

Bayleef is weak to ice, poison, bug, fire, and flying pokemon. 

# Today's Lesson: 
### Move the code from the previous lesson into a function.

If a piece of code does something that we may want to do again it's a good idea to turn the code into a function!

<u>In the cell below create a function called `extreme_weakness_types` that:</u> 
1. Receives the name of a pokemon
2. Isolates the weakness data for that pokemon
3. Returns a list of all types the given pokemon is extremely weak to.


```python
def extreme_weakness_types(pokemon):
    weakness_data = data[pokemon]['weakness']
    
    weakness_types = []

    for weakness in weakness_data.keys():
        if weakness_data[weakness] == 2:
            weakness_types.append(weakness)

    return weakness_types
```

### Previous Lesson:

In the cell below, use the weakness_types list to identify pokemon that have one of those types, and append those pokemon to a list named ```bayleef_weakness```. 

>**Hint** The code will be very similar to the code for step 2.

>**Hint** Make sure your list doesn't contain duplicates of the same pokemon!

Run the cell below to test your code! ⬇️

# Today's lesson: Move the code above into a function!

<u>In the cell below create a function called `pokemon_with_type` that:</u>
1. Receives the name of a pokemon type
2. Returns the name for every pokemon with the given type.


```python
def pokemon_with_type(pokemon_type):
    pokemon_names = set()
    for key in data.keys():
        if data[key]['stats']['type1'] == pokemon_type:
            pokemon_names.add(key)
        elif data[key]['stats']['type2'] == pokemon_type:
            pokemon_names.add(key)

    pokemon_names = list(pokemon_names)
    return pokemon_names
```

**Run the cell below to test your code!**


```python
def stat_by_type(stat, pokemon_type):
    pokemon_names = pokemon_with_type(pokemon_type)
    stats = [data[name]['stats'][stat] for name in pokemon_names]
    return stats
```

**Run the cell below to test your code**


```python
import matplotlib.pyplot as plt

def mean(array):
    return sum(array)/len(array)

def compare_types(stat, type1, type2):
    type1_stats = stat_by_type(stat, type1)
    type2_stats = stat_by_type(stat, type2)
    print('                        Report')
    print('======================================================')
    print(f'Number of {type1} pokemon: ', len(type1_stats))
    print(f'Number of {type2} pokemon: ', len(type2_stats))
    print('––––––––––––––––––––––––––––––––––––––––––––––––––––––')
    print(f'{type1} mean {stat}: ', mean(type1_stats))
    print(f'{type2} mean {stat}: ', mean(type2_stats))
    
    plt.hist(type1_stats, alpha=.5, label=type1)
    plt.hist(type2_stats, alpha=.5, label=type2)
    plt.legend()
    plt.title(f'{type1} vs. {type2} –– {stat}')
    plt.show()
```
