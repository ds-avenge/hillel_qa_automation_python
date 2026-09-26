from pathlib import Path
from datetime import datetime
import logging

base_path = Path(__file__).parent
log_file = base_path / "hblog.txt"
target_key = "Key TSTFEED0300|7E3E|0400"

log_output = base_path / "hb_test.log"

logging.basicConfig(
    filename=log_output,
    level=logging.WARNING,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

if not log_file.exists():
    raise FileNotFoundError(f"File not found: {log_file}")

with open(log_file, "r") as f:
    filtered_log = [line for line in f if target_key in line]

if not filtered_log:
    raise ValueError(f"No entries found for key: {target_key}")

# print(len(filtered_log))
# print('\n'.join(filtered_log))

times = []

for line in filtered_log:
    timestamp_index = line.find("Timestamp ")
    if timestamp_index == -1:
        continue

    start = timestamp_index + len("Timestamp ")
    time_str = line[start:start + 8]

    try:
        time_obj = datetime.strptime(time_str, "%H:%M:%S")
    except ValueError:
        logging.error(f"Invalid timestamp format: {time_str}")
        continue

    times.append(time_obj)

# print(times)
if len(times) < 2:
    raise ValueError("Not enough timestamps for heartbeat analysis")

for i in range(len(times) - 1):
    time_diff = (times[i] - times[i + 1]).total_seconds()

    if 31 < time_diff < 33:
        logging.warning(f"Heartbeat delay: {time_diff} seconds at {times[i].strftime('%H:%M:%S')}")
    elif time_diff >= 33:
        logging.error(f"Heartbeat delay: {time_diff} seconds at {times[i].strftime('%H:%M:%S')}")
