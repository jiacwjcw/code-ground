/**
 * @param {number[]} array
 * @return {void}, please modify directly array in-place instead.
 */
var move = function(array) {

    var position = 0;

    for (var index = 0; index < array.length; index++) {
        var n = array[index];
        if (n != 0) {
            console.log(position);
            array[position++] = n; // stuck1
            console.log(position);
        }
    }

    for (position; position < array.length; position++) { // stuck 2
        array[position] = 0;
    }

    return array
};

console.log(move([0, 1, 0, 3, 12]));
