<script setup>
import { ref, onMounted } from 'vue'

// const Url = 'http://localhost'
const Url = 'http://3.19.219.96'

// reactive state
const mtt = ref()
const mtb = ref()
const mtd = ref()
const waiters = ref([])
const maxProducts = ref({})
const categories = ref({})
const selectedWaiter = ref("")
const waiterBilling = ref(0)
const waiterOrders = ref(0)
const zones = ref([])
const selectedZone = ref("")
const zoneMeanBilling = ref(0)
const zoneMeanTime = ref(0)
const selectedPeriod = ref("mes")



async function fetchSelectedWaiter(){
  fetch(`${Url}:5000/waiter-info?name=${selectedWaiter.value}`)
    .then(res => res.json())
    .then(data => {
      waiterBilling.value = data.total_billing
      waiterOrders.value = data.total_orders
    })

}

async function fetchSelectedZone(){
  fetch(`${Url}:5000/zone-info?zone=${selectedZone.value}`)
    .then(res => res.json())
    .then(data => {
      zoneMeanBilling.value = data.mean_billing
      zoneMeanTime.value = data.mean_time
    })

}


// lifecycle hooks
onMounted(() => {
  fetch(`${Url}:5000/general-data`)
    .then(res => res.json())
    .then(data => {
      mtt.value = data.mtt
      mtb.value = Math.round(data.mtb)
      mtd.value = data.mtd.toFixed(1)
      zones.value = data.zones
      waiters.value = data.waiters 
      maxProducts.value = Object.entries(data.products).sort((x, y) => y[1] - x[1]).slice(0,3)
      categories.value = data.categories
    })

})

</script>

<template>
  <div class="main-col">
    <div class="gen-info card">
      <div class="mini-card">
        <p class="t1">Promedio de estadía por mesa</p>
        <p> {{ mtt }}</p>
      </div>
      <div class="mini-card">
        <p class="t1">Promedio de monto por mesa</p>
        <p> {{ mtb }}</p>
      </div>
      <div class="mini-card">
        <p class="t1">Promedio de personas por mesa</p>
        <p> {{ mtd }}</p>
      </div>
      <div class="mini-card">
        <p class="t1">Productos más vendidos</p>
        <p v-for="product in maxProducts">{{product[0]}}: {{product[1]}}</p>
      </div>
    </div>

    <div class="bottom-col">
      <div class="waiter-info card" >
        <p class="t1">Información específica mesero</p>
        <label for="waiters">Elige un mesero:</label>

        <select v-model="selectedWaiter" @change="fetchSelectedWaiter()">
          <option v-for="waiter in waiters" :value="waiter">{{ waiter }}</option>
        </select>

        <p v-if="waiterBilling !== 0 ">Monto total de ventas: {{waiterBilling}}</p>
        <p v-if="waiterOrders !== 0 ">Monto total de ventas: {{waiterOrders}}</p>
      </div>


      <div class="zone-info card" >
        <p class="t1">Información específica zona</p>
        <label for="zones">Elige una zona:</label>

        <select v-model="selectedZone" @change="fetchSelectedZone()">
          <option v-for="zone in zones" :value="zone">{{ zone }}</option>
        </select>

        <p v-if="zoneMeanBilling !== 0 ">Monto promedio por mesa: {{zoneMeanBilling}}</p>
        <p v-if="zoneMeanTime !== 0 ">Tiempo promedio de estadía: {{zoneMeanTime}}</p>
      </div>

      <div class="chart-box card">
        <label for="periods">Elige un periodo:</label>
        <select v-model="selectedPeriod" @change="fetchSelectedPeriod()">
          <option value="dia">día</option>
          <option value="semana">semana</option>
          <option value="mes" selected="true">mes</option>
        </select>
      </div>

    </div>
  </div>
</template>

<style scoped>

.main-col {
  display: flex;
  flex-direction: column;
  height: 100%;
}

.gen-info {
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  align-self: center;
  width: 95%;
}

.bottom-col { 
  display: flex;
  flex-direction: row;
  height: 100%;
}

.waiter-info {
  width: 25%;
  height: 150px;
}

.zone-info {
  width: 25%;
}

.chart-box {
  width: 50%;
}

.card {
  margin: 20px;
  padding: 20px;
  min-height: 200px;
  border-radius: 10px;
  box-shadow: 0px 6px 10px rgba(0, 0, 0, 0.25);
  transition: all 0.2s;
  background-color: white;
}

.mini-card {
  margin: 20px;
  padding: 10px;
  width: 90%;
  /* border-radius: 10px;
  box-shadow: 0px 6px 10px rgba(0, 0, 0, 0.25); */
  display: flex;
  flex-direction: column;
  align-items: center;

  /* min-height: 250px; */
}

.t1 {
  
  font-family: Helvetica;
  font-size: 20px;
}

</style>