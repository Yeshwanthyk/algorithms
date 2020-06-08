function meetingRooms(intervals) {
  const starts = [];
  const ends = [];

  intervals.forEach((interval, i) => {
    starts[i] = interval[0];
    ends[i] = interval[1];
  });

  starts.sort((a, b) => a - b);
  ends.sort((a, b) => a - b);

  let rooms = 0;
  let endIdx = 0;

  for (i = 0; i < intervals.length; i++) {
    if (starts[i] < ends[endIdx]) {
      rooms++;
    } else {
      endIdx++;
    }
  }

  return rooms;
}
