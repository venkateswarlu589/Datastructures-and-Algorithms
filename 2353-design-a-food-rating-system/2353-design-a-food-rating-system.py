class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):

        self.cuisine_heap_lookup = {}

        self.cuisine_hash_lookup = {}

        self.cuisine_reverse_lookup = {}
        
        for cuisine in cuisines:
            self.cuisine_heap_lookup[cuisine] = []
            self.cuisine_hash_lookup[cuisine] = {}
            
        n = len(foods)
        for index in range(n):
            heap_lookup = self.cuisine_heap_lookup[cuisines[index]]
            hash_lookup = self.cuisine_hash_lookup[cuisines[index]]
            
            self.cuisine_reverse_lookup[foods[index]] = cuisines[index]
            heapq.heappush(heap_lookup, [-ratings[index], foods[index]])
            hash_lookup[foods[index]] = ratings[index]

    def changeRating(self, food: str, newRating: int) -> None:
        
        cuisine = self.cuisine_reverse_lookup[food]
        heap_lookup = self.cuisine_heap_lookup[cuisine]
        hash_lookup = self.cuisine_hash_lookup[cuisine]
        
        heapq.heappush(heap_lookup, [-newRating, food])
        hash_lookup[food] = newRating
 
    def highestRated(self, cuisine: str) -> str:
        heap_lookup = self.cuisine_heap_lookup[cuisine]
        hash_lookup = self.cuisine_hash_lookup[cuisine]
 
        while heap_lookup and -heap_lookup[0][0] != hash_lookup[heap_lookup[0][1]]:
            heapq.heappop(heap_lookup)
        
        return heap_lookup[0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)