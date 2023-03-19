function iterator(rangeStart, rangeEnd) {
  if (rangeStart == 0 && rangeEnd == 0) {
    return null;
  }

  var iterate = function* (start = 0, end = 5, step = 1) {
    for (let i = start; i <= end; i += step) {
      yield i;
    }
  };
  var values = iterate(rangeStart, rangeEnd);
  var pointer = values.next();
  var tmp = [];

  while (pointer.value != undefined) {
    tmp.push(pointer.value);
    pointer = values.next();
  }

  return tmp.join(',');
}
