

BUILD_SCRIPT=buildscripts/build.py
COMMON_OPTIONS= -Q --jobs=6 --silent

all:
	$(BUILD_SCRIPT) $(COMMON_OPTIONS)

helloworld:
	$(BUILD_SCRIPT) $(COMMON_OPTIONS) $@

lint:
	$(BUILD_SCRIPT) $(COMMON_OPTIONS) $@

clean:
	$(BUILD_SCRIPT) $(COMMON_OPTIONS) -c
	rm -rf build config.log
