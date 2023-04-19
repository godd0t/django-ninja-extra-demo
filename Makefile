define HELP

Manage $(PROJECTNAME). Usage:

make lint           	Run linter
make format         	Run formatter
make test           	Run tests

endef

export HELP


lint:
	 @bash ./scripts/lint.sh

format:
	@bash ./scripts/format.sh

test:
	@bash ./scripts/test.sh

.PHONY: run-command python django collectstatic \
		super-user add-initial-data clear-media make-migrations migrate \
		pre-commit all help manage.py makemigrations
