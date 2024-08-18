function adjustValue(e, unit) {
    let value = parseInt(e.target.value.replace(unit, '') || '0');
    
    if (e.key === 'ArrowUp') {
        value += 1;
    } else if (e.key === 'ArrowDown') {
        value = value > 0 ? value - 1 : 0;
    }

    e.target.value = value + unit;
}

document.getElementById('altura').addEventListener('keydown', function(e) {
    adjustValue(e, 'cm');
});

document.getElementById('peso').addEventListener('keydown', function(e) {
    adjustValue(e, 'kg');
});