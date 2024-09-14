def read_binary_file(file_path):
    with open(file_path, 'rb') as file:
        return file.read()

def convert_to_hex(byte_data):
    # Agrupamos los datos de 8 en 8
    byte_data = [byte_data[i:i+8] for i in range(0, len(byte_data), 8)]
    print ("La longitud de byte_data es: ", len(byte_data))
    #print (byte_data)
    # Convertimos cada byte a su representación en hexadecimal
    resu = []
    for i in range(len(byte_data)):
        byte = sum([byte_data[i][j] << j for j in range(8)])
        print ('El valor de byte es: ', byte)
        # Añadimos el valor en hexadecimal a la lista resu
        resu.append(f'0x{byte:02X}')


    return resu

def write_hex_file(hex_data, output_path):
    with open(output_path, 'w') as file:
        # Separamos los valores por comas y ponemos un salto de linea cada 16 valores
        file.write ('static const char font_8x8[] = {\n\t')
        slice_size = 16
        for i in range(0, len(hex_data), slice_size):
            file.write(', '.join(hex_data[i:i+slice_size]))
            file.write(',\n\t')
        file.write('};')
        

def main(input_file, output_file):
    binary_data = read_binary_file(input_file)
    hex_data = convert_to_hex(binary_data)
    write_hex_file(hex_data, output_file)

if __name__ == "__main__":
    input_file = './font_8x8_ega.data'
    output_file = './font_8x8.h'
    main(input_file, output_file)