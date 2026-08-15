class Solution {
    public int[][] merge(int[][] intervals) {
        if (intervals.length < 2){
            return intervals;
        }
        Arrays.sort(intervals, (a,b) -> Integer.compare(a[0], b[0]));
        int[] curr = intervals[0];
        ArrayList<int[]> answer = new ArrayList<>();
        for(int[] next : intervals){
            int currEnd = curr[1];
            int nextStart = next[0];
            int nextEnd = next[1];
            if(currEnd >= nextStart){
                curr[1] = Math.max(nextEnd, currEnd);
            }
            else{
                answer.add(curr);
                curr = next;
            }
        }
        answer.add(curr);
        return answer.toArray(new int[answer.size()][2]);
    }
}