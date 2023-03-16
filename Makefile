# ===== Docker Compose =====

compose-build:
	echo "Starting Docker Build"
	docker-compose -f docker-compose.dev.yaml build

compose-up:
	echo "Starting Docker Up"
	docker-compose -f docker-compose.dev.yaml up -d

compose-ps:
	echo "Starting Docker Ps"
	docker-compose -f docker-compose.dev.yaml ps

compose-logs:
	echo "Starting Docker Logs"
	docker-compose -f docker-compose.dev.yaml logs

compose-down:
	echo "Starting Docker Down"
	docker-compose -f docker-compose.dev.yaml down --remove-orphans