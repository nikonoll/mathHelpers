#calculating the similarity to an ideal car

idealCar = {
    :price => 5000.0,
    :km => 50000.0,
    :ps => 120.0,
    :diesel => 1.0,
    :wheels => 1.0,
    :drivebelt => 1.0
}

weights = {
    :price => 1.0,
    :km => 1.0,
    :ps => 0.2,
    :diesel => 0.6,
    :wheels => 0.2,
    :drivebelt => 0.2
}

sumWeights = (weights[:price]+weights[:km]+weights[:ps]+weights[:diesel]+weights[:wheels]+weights[:drivebelt])

#-------------
#---car data--
#-------------
muc = {
    :price => 8000.0,
    :km => 90500.0,
    :ps => 105.0,
    :diesel => 1.0,
    :wheels => 1.0,
    :drivebelt => 0.0
}
silver = {
    :price => 8000.0,
    :km => 96000.0,
    :ps => 102.0,
    :diesel => 0.0,
    :wheels => 0.0,
    :drivebelt => 0.0
}
landau = {
    :price => 7999.0,
    :km => 217505.0,
    :ps => 140.0,
    :diesel => 1.0,
    :wheels => 1.0,
    :drivebelt => 1.0
}
def simpleSim(x,y)
    dif = (x-y).abs
    sum = x+y
    sim = dif/sum
    return sim
end

def binarySim(x,y)
    if(x == y)
        return 1
    else
        return 0
    end
end

def calculateValue (car, icar, w)
    carSims = {
        :price => w[:price]*(simpleSim(car[:price], icar[:price])),
        :km => w[:km]*(simpleSim(car[:km], icar[:km])),
        :ps => w[:ps]*(simpleSim(car[:km], icar[:km])),
        :diesel => w[:diesel]*(binarySim(car[:diesel], icar[:diesel])),
        :wheels => w[:wheels]*(binarySim(car[:wheels], icar[:wheels])),
        :drivebelt => w[:drivebelt]*(binarySim(car[:drivebelt], icar[:drivebelt])) 
   }
    return carSims
end

res = calculateValue(muc, idealCar, weights)
puts 'calculated sims muc'
puts res 
puts '-----------------'
puts 'total sim'
puts (res[:price]+res[:km]+res[:ps]+res[:diesel]+res[:wheels]+res[:drivebelt])/sumWeights

res2 = calculateValue(landau, idealCar, weights)
puts 'calculated sims for landau'
puts res2 
puts '-----------------'
puts 'total sim'
puts (res2[:price]+res2[:km]+res2[:ps]+res2[:diesel]+res2[:wheels]+res2[:drivebelt])/sumWeights

