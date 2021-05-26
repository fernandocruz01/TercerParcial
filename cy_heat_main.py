from __future__ import print_function
import time
import argparse
from io import open

from cy_heat import init_fields, write_field, iterate


def main(input_file='bottle_large.dat', a=0.5, dx=0.1, dy=0.1, 
         timesteps=200, image_interval=4000, file='heat.txt'):

    field, field0 = init_fields(input_file)

    print("Heat equation solver: {}".format(input_file))
    print("Diffusion constant: {}".format(a))
    print("Input file: {}".format(input_file))
    print("Parameters")
    print("----------")
    print("  nx={} ny={} dx={} dy={}".format(field.shape[0], field.shape[1],
                                             dx, dy))
    print("  time steps={}  image interval={}".format(timesteps,
                                                         image_interval))

    # Trazar/guardar el campo inicial
    write_field(field, 0)
    t0 = time.time()
    iterate(field, field0, a, dx, dy, timesteps, image_interval)
    t1 = time.time()
    write_field(field, timesteps)
   
    file_aux = open(file, 'a')
    file_aux = file_aux.write("with file {} finshed in {} ns\n".format(input_file,t1-t0))

    print("Simulation finished in {0} s".format(t1-t0))

if __name__ == '__main__':

    bottles= {
        'bottle': 'bottle.dat',
        'bottle_medium': 'bottle_medium.dat',
        'bottle_large': 'bottle_large.dat',
    }
    file = 'results/cython_heat.txt'
    for i in range(3):
        for bottle in bottles:
            
            parser = argparse.ArgumentParser(description='Heat equation')
            parser.add_argument('-dx', type=float, default=0.01,
                                help='grid spacing in x-direction')
            parser.add_argument('-dy', type=float, default=0.01,
                                help='grid spacing in y-direction')
            parser.add_argument('-a', type=float, default=0.5,
                                help='diffusion constant')
            parser.add_argument('-n', type=int, default=200,
                                help='number of time steps')
            parser.add_argument('-i', type=int, default=4000,
                                help='image interval')
            parser.add_argument('-f', type=str, default=bottles[bottle], 
                                help='input file')

            args = parser.parse_args()
            main(args.f, args.a, args.dx, args.dy, args.n, args.i, file)

