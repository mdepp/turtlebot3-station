.phony: all
all: build

.phony: check-dependencies
check-dependencies:
	rosdep check --from-paths src

.PHONY: build
build: check-dependencies
	colcon build --cmake-args -DCMAKE_EXPORT_COMPILE_COMMANDS=ON --symlink-install

.PHONY: test
test: check-dependencies
	colcon test

.PHONY: clean
clean:
	rm -rf build/ install/ log/

.PHONY: rosdep
rosdep:
	rosdep install --from-paths src -y
