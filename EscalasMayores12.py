### Programa que devuelve las 


import os
from os.path import basename
import sys
sys.path.append(".")


class Escalas():

    def __init__(self) -> None:
        self.circulo_quintas_mayores = ['C' ,'G' ,'D' ,'A'  ,'E'  ,'B'  ,'Gb' ,'Db' ,'Ab','Eb','Bb','F']
        self.circulo_quintas_menores = ['Am','Em','Bm','F#m','C#m','G#m','Ebm','Bbm','Fm','Cm','Gm','Dm']
        
        self.formulaEscalaMayor = [2,2,1,2,2,2,1]
        self.escalaCromatica = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B',  'C','C#','D','D#','E','F','F#']

        self.sharpsNflats = {
            'C#' :'Db',
            'C#m':'Dbm',
            'D#' :'Eb',
            'D#m':'Ebm',
            'F#' :'Gb',
            'F#m':'Gbm',
            'G#' :'Ab',
            'G#m':'Abm',
            'A#' :'Bb',
            'A#m':'Bbm',
        }

        self.romanNumbers = {
            1:'I   ',
            2:'II  ',
            3:'III ',
            4:'IV  ',
            5:'V   ',
            6:'VI  ',
            7:'VII°',
        }

    def get_sharp_from_flat(self,val):
        for key, value in self.sharpsNflats.items():
            if val == value:
                return key
        return "El acorde # no existe"

    def escaleFromNote(self,note,chords_too=False):
        sharp = False
        if '#' in note:
            note = self.sharpsNflats.get(note)
            sharp = True

        if note in self.circulo_quintas_mayores:
            index = self.circulo_quintas_mayores.index(note)
            scale = [note]
            if note == 'C':
                scale.append(self.circulo_quintas_menores[len(self.circulo_quintas_menores)-1])
                scale.append(self.circulo_quintas_menores[index+1])
                scale.append(self.circulo_quintas_mayores[len(self.circulo_quintas_menores)-1])
                scale.append(self.circulo_quintas_mayores[index+1])
                scale.append(self.circulo_quintas_menores[index])
                scale.append(self.circulo_quintas_menores[index+2])
            elif note == 'F':
                scale.append(self.circulo_quintas_menores[index-1])
                scale.append(self.circulo_quintas_menores[0])
                scale.append(self.circulo_quintas_mayores[index-1])
                scale.append(self.circulo_quintas_mayores[0])
                scale.append(self.circulo_quintas_menores[index])
                scale.append(self.circulo_quintas_menores[1])
            elif note == 'Bb':
                scale.append(self.circulo_quintas_menores[index-1])
                scale.append(self.circulo_quintas_menores[index+1])
                scale.append(self.circulo_quintas_mayores[index-1])
                scale.append(self.circulo_quintas_menores[index])
                scale.append(self.circulo_quintas_mayores[index+1])
                scale.append(self.circulo_quintas_menores[0])
            else:                
                scale.append(self.circulo_quintas_menores[index-1])
                scale.append(self.circulo_quintas_menores[index+1])
                scale.append(self.circulo_quintas_mayores[index-1])
                scale.append(self.circulo_quintas_mayores[index+1])
                scale.append(self.circulo_quintas_menores[index])
                scale.append(self.circulo_quintas_menores[index+2])

            
            if sharp:
                arranged_scale = []
                for chord in scale:
                    if('b' in chord):
                        arranged_scale.append(self.get_sharp_from_flat(chord))
                    else:
                        arranged_scale.append(chord)
                
                #last_chord = arranged_scale.pop(len(arranged_scale)-1)
                #last_diminish_chord = last_chord +'(dim)'
                #arranged_scale.append(last_diminish_chord)
                for c in range(0,len(arranged_scale)):
                    if chords_too:
                        print(self.romanNumbers.get(c+1) + ': ' + arranged_scale[c] + ' - ' + self.notesFromChord(arranged_scale[c]))
                    else:
                        print(self.romanNumbers.get(c+1) + ': ' + arranged_scale[c] )
                #return arranged_scale
            else:
                #last_chord = scale.pop(len(scale)-1)
                #last_diminish_chord = last_chord +'(dim)'
                #scale.append(last_diminish_chord)
                for c in range(0,len(scale)):
                    current_chord = scale[c]
                    if '#' in current_chord:
                            current_chord = self.sharpsNflats.get(current_chord)
                            
                    if chords_too:
                        print(self.romanNumbers.get(c+1) + ': ' + scale[c] + ' - ' + str(self.notesFromChord(scale[c])))
                    else:
                        print(self.romanNumbers.get(c+1) + ': ' + scale[c] )
                #return scale
        else:   
            print('That note does not exist!')
            return None

    def notesFromChord(self,chord):
        # Eliminamos indicador de acorde menor, solo necesitamos el nombre, ya que la formula de la escala mayor
        # nos ayudara a construir cada acorde mayor o menor perteneciente a la escala en cuestion.

        minor = False
        flat = False
        if 'm' in chord and 'b' in chord:
            chord = chord.replace('m','') 
            chord = self.get_sharp_from_flat(chord)
            minor = True
            flat = True
        elif 'b' in chord:
            chord = self.get_sharp_from_flat(chord)
        elif 'm' in chord:
            chord = chord.replace('m','') 
            minor = True

        if chord in self.escalaCromatica:
            index = self.escalaCromatica.index(chord)
            chord_notes = []

            if minor:
                first_note = 1 + index
                third_note = 4 + index
                fifth_note = 8 + index
                chord_notes.append(self.escalaCromatica[first_note-1]) #-1 por corrimiento en array
                chord_notes.append(self.escalaCromatica[third_note-1])
                chord_notes.append(self.escalaCromatica[fifth_note-1])
            else:
                first_note = 1 + index
                third_note = 5 + index
                fifth_note = 8 + index
                chord_notes.append(self.escalaCromatica[first_note-1])
                chord_notes.append(self.escalaCromatica[third_note-1])
                chord_notes.append(self.escalaCromatica[fifth_note-1])

            if flat:
                arranged_chord_notes = []
                for chord in chord_notes:
                    arranged_chord_notes.append(self.sharpsNflats.get(chord))
                return arranged_chord_notes
            else:
                return chord_notes
        else:
            print('That note does not exist!')
            return None
    

def menu():
    #os.system('cls')
    print("Seleccione una opcion.")
    print("\t1. Escala a partir de nota")
    print("\t2. Notas a partir de acorde")
    print("\t3. Escala y acordes a partir de nota")
    print("\t4. Adios musical")


def main():
    obj = Escalas()


    while True:

        menu()
        option = input('Ingrese una opcion: ')

        if(option == '1'):
            note_name = input('Ingrese el nombre de la nota para obtener una escala: ')
            obj.escaleFromNote(note_name)

        elif(option == '2'):
            chord_name = input('Ingrese el acorde para obtener sus primeras tres notas: ')
            chord = obj.notesFromChord(chord_name)
            print(chord)

        elif(option == '3'):
            note_name = input('Ingrese el nombre de la nota para obtener una escala y sus acordes: ')
            obj.escaleFromNote(note_name,True)

        elif(option == '4'):

            print('Adios')
            break


if __name__ == "__main__":
    main()


