all:
	python3 setup.py build_ext --inplace
	mkdir results
clean:
	rm -rf build *.so cyfib.c *.c *.html results
