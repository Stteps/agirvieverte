FROM busybox:latest

# Note: This container is used for copying git-hooks script into the appropriate folder in the docker app environment
# Note: This container starts, it copy files, then stop.
ENTRYPOINT sh -c "cd /tmp/hooks && ls | xargs chmod +x && cd /tmp/.git/hooks && find ../../hooks -type f -exec ln -sf {} /tmp/.git/hooks/ \; && echo 'githooks installed'"
