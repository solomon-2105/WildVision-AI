<template>

<div class="card">

<h2>Detection History</h2>

<div v-if="history.length==0" class="empty">
No detections yet
</div>

<div v-for="item in history" :key="item.id" class="history-item">

<span>{{item.predicted_class}}</span>

<span>{{item.confidence}}</span>

</div>

</div>

</template>

<script>

export default{

props:["history"]

}

</script>

<style>

.card{
background:#1e293b;
padding:30px;
border-radius:12px;
box-shadow:0 10px 20px rgba(0,0,0,0.4);
}

.card h2{
margin-top:0;
color:#38bdf8;
}

.history-item{
display:flex;
justify-content:space-between;
padding:10px;
border-bottom:1px solid #334155;
}

.history-item span:first-child{
color:#e2e8f0;
}

.history-item span:last-child{
color:#38bdf8;
}

.empty{
color:#64748b;
}

</style>