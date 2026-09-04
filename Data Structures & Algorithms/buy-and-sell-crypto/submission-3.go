func maxProfit(prices []int) int {
    minPrice := math.MaxInt
	maxProfit := 0
    for _, price := range prices {
		if price < minPrice {
            minPrice = price
		} else if price-minPrice > maxProfit {
            maxProfit = price - minPrice
		}
	}
	return maxProfit
}
