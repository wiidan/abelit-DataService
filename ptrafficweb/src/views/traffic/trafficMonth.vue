<template>
  <div>
    <div style="background:#409EFF;color:#ffffff;padding:10px;">花果园购物中心1-疫情期各入口客流统计</div>
    <el-row>
      <el-col>
        <div class="block">
          <span class="demonstration mx-5">按月查询</span>
          <el-date-picker v-model="value2" type="month" placeholder="选择月"></el-date-picker>
          <el-button icon="el-icon-search" circle class="ma-5" :disabled="disabled" @click="btn"></el-button>
        </div>
      </el-col>
    </el-row>
    <el-row>
      <el-col>
        <!-- <el-table
          :data="tableData"
          v-loading="loading"
          :row-class-name="tableRowClassName"
          element-loading-text="客流数据加载中..."
          border
          show-summary
          :summary-method="getSummaries"
          style="width: 100%"
          :default-sort="{ prop: 'date', order: 'descending' }"
        >
          <el-table-column type="index" width="50"></el-table-column>
          <el-table-column prop="tbheader" label="入口"></el-table-column>
          <el-table-column prop="tbdata" :label="titleLabel" :render-header="renderheader"></el-table-column>
        </el-table>-->
        <el-table
          :data="tableData"
          v-loading="loading"
          style="width: 1192px"
          show-summary
          :summary-method="getSummaries"
        >
          <el-table-column type="index" width="70" label="序号"></el-table-column>
          <el-table-column prop="pdate" label="日期" width="120" :formatter="dateFormat"></el-table-column>
          <el-table-column label="花果园购物中心1-疫情期各入口客流统计">
            <el-table-column prop="psquare" label="沿湖广场" :formatter="numberFormat" width="100"></el-table-column>
            <el-table-column prop="phm" label="H&M" :formatter="numberFormat" width="100"></el-table-column>
            <el-table-column prop="pgateway" label="人行天桥(乐转旁)" :formatter="numberFormat" width="100"></el-table-column>
            <el-table-column prop="pgatewaypiz" label="人行天桥(必胜客旁)" :formatter="numberFormat" width="100"></el-table-column>
            <el-table-column prop="pkfc" label="肯德基" :formatter="numberFormat" width="100"></el-table-column>
            <el-table-column prop="pqbj" label="一楼黔宝金店旁" :formatter="numberFormat" width="100"></el-table-column>
            <el-table-column prop="pck" label="CKJeans" :formatter="numberFormat" width="100"></el-table-column>
            <el-table-column prop="prest" label="食尚汇门厅旁" :formatter="numberFormat" width="100"></el-table-column>
            <el-table-column prop="pparking" label="停车场" :formatter="numberFormat" width="100"></el-table-column>
            <el-table-column prop="pall" label="总计" :formatter="numberFormat" width="100"></el-table-column>
          </el-table-column>
        </el-table>
      </el-col>
    </el-row>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";
import Axios from "axios";
import * as fecha from "element-ui/lib/utils/date";
@Component
export default class ComponentName extends Vue {
  value2: Date = new Date();
  loading: boolean = false;
  disabled: boolean = false;
  tableData: Array<object> = [];
  titleLabel: string = " 客流(人次)" + "/" + "10:00~22:00";

  pickerOptions: any = {
    disabledDate(time: any) {
      return time.getTime() >= Date.now();
    }
  };

  // public value2: Array<string> = [
  //   this.formatDate(
  //     new Date(new Date().setTime(new Date().getTime() - 3600 * 1000 * 24 * 1))
  //   ),
  //   this.formatDate(
  //     new Date(new Date().setTime(new Date().getTime() - 3600 * 1000 * 24 * 1))
  //   ),
  // ];
  //public value2:string=this.formatDate(new Date(new Date().setTime(new Date().getTime() - 3600 * 1000 * 24 * 1)));

  private renderheader(h: any, { column, $index }: any) {
    return h("span", {}, [
      h("span", {}, column.label.split("/")[0]),
      h("br"),
      h("span", {}, column.label.split("/")[1])
    ]);
  }

  public thousandSeparator(num: number) {
    return (
      num &&
      (num.toString().indexOf(".") != -1
        ? num.toString().replace(/(\d)(?=(\d{3})+\.)/g, function($1, $2) {
            return $2 + ",";
          })
        : num.toString().replace(/(\d)(?=(\d{3})+\b)/g, function($1, $2) {
            return $2 + ",";
          }))
    );
  }

  btn() {
    //console.log(this.startTime.setTime(this.star));
    // console.log(this.value2);
    // console.log(this.thousandSeparator(4656262.262))

    // this.tableData = [];
    //console.log(this.value2.toString())
    //console.log(this.re_month(this.value2)[0]);
    //console.log(this.re_month(this.value2)[1]);
    this.getData(
      this.formatDate(this.re_month(this.value2)[0]),
      this.formatDate(this.re_month(this.value2)[1])
    );
  }
  private mounted() {
    //console.log(this.value2);
    //this.getData(this.value2[0].toString(), this.value2[1].toString());
  }
  public getData(s: string, d: string) {
    this.disabled = true;
    this.loading = true;
    Axios.get("http://58.42.231.98:5060/api/ptraffic/date", {
      params: {
        start: s,
        end: d
      }
    })
      .then(res => {
        if (res.status == 200) {
          //{"tbheader":"psquare","tbdata":2000},{"tbheader":"phm","tbdata":3000}
          this.tableData = [];
          res.data.forEach((item,index)=>{
            if(new Date(item.pdate)<new Date("2020-05-16")){
              item.pgatewaypiz=0;
              item.pkfc=0;
              item.prest=0;
            }
            if(new Date(item.pdate)<new Date("2020-05-24")){
              item.pck=0;
              item.pqbj=0;
              
            }
            //   <el-table-column prop="psquare" label="沿湖广场" :formatter="numberFormat" width="100"></el-table-column>
            // <el-table-column prop="phm" label="H&M" :formatter="numberFormat" width="100"></el-table-column>
            // <el-table-column prop="pgateway" label="人行天桥(乐转旁)" :formatter="numberFormat" width="100"></el-table-column>
            // <el-table-column prop="pgatewaypiz" label="人行天桥(必胜客旁)" :formatter="numberFormat" width="100"></el-table-column>
            // <el-table-column prop="pkfc" label="肯德基" :formatter="numberFormat" width="100"></el-table-column>
            // <el-table-column prop="prest" label="食尚汇门厅旁" :formatter="numberFormat" width="100"></el-table-column>
            // <el-table-column prop="pparking" label="停车场" :formatter="numberFormat" width="100"></el-table-column>
            item.pall=item.psquare+item.phm+item.pgateway+item.pgatewaypiz+item.pkfc+item.prest+item.pparking+item.pck+item.pqbj
          
          })
          this.tableData = res.data;
          
          // let resData = res.data[0];
          // let tbheader;
          // for (let j in resData) {
          //   switch (j) {
          //     case "psquare":
          //       tbheader = "沿湖广场";
          //       break;
          //     case "phm":
          //       tbheader = "H&M";
          //       break;
          //     case "pgateway":
          //       tbheader = "人行天桥";
          //       break;
          //     case "pparking":
          //       tbheader = "停车场";
          //       break;
          //     default:
          //       continue;
          //   }

          //   this.tableData.push({
          //     tbheader: tbheader,
          //     tbdata: this.thousandSeparator(resData[j]),
          //   });
          //   //console.log(j+":"+resData[j]);
          // }
          this.loading = false;
          this.disabled = false;
          //console.log(this.tableData);
        }
      })
      .catch(err => {
        console.log(err);
        this.disabled = false;
      });
  }

  public formatDate(date: Date) {
    var d = date,
      month = "" + (d.getMonth() + 1),
      day = "" + d.getDate(),
      year = d.getFullYear();

    if (month.length < 2) month = "0" + month;
    if (day.length < 2) day = "0" + day;

    return [year, month, day].join("-");
  }
  public getSummaries(param: any) {
    //console.log(param);
    const { columns, data } = param;
    const sums: any = [];
    columns.forEach((column: any, index: any) => {
      if (index === 0) {
        sums[index] = "总计";
        return;
      }
      const values = data.map((item: any) => Number(item[column.property]));
      if (!values.every((value: any) => isNaN(value))) {
        sums[index] = values.reduce((prev: any, curr: any) => {
          const value = Number(curr);
          if (!isNaN(value)) {
            return prev + curr;
          } else {
            return prev;
          }
        }, 0);
        sums[index] = sums[index].toLocaleString();
      } else {
        sums[index] = "N/A";
      }
      return sums;
      // const values:any = data.map((item: any) => Number(item[column.property].replace(',','')));

      // if (!values.every((value: any) => isNaN(value))) {
      //   sums[index] = values.reduce((prev:any, curr:any) => {
      //     const value = Number(curr);
      //     if (!isNaN(value)) {
      //       return prev + curr;
      //     } else {
      //       return prev;
      //     }
      //   }, 0);
      //   sums[index] = this.thousandSeparator(sums[index]) + '';
      // } else {
      //   sums[index] = '';
      // }
    });

    //console.log(sums)

    return sums;
  }
  public tableRowClassName({ row, rowIndex }: any) {
    //console.log(row['tbdata'].replace(",",""))
    if (row["tbdata"].replace(",", "") >= 5000) {
      return "warning-row";
    }
    return "";
  }
  public re_month(d: Date) {
    let re_arr = [];
    let now = new Date(); //当前日期
    let nowMonth = d.getMonth(); //当前月
    let nowYear = d.getFullYear(); //当前年
    //本月的开始时间
    let monthStartDate = new Date(nowYear, nowMonth, 1);
    //本月的结束时间
    let monthEndDate = new Date(nowYear, nowMonth + 1, 0);
    // let timeStar=Date.parse(monthStartDate)/1000;//s
    // let timeEnd=Date.parse(monthEndDate)/1000;//s
    re_arr = [monthStartDate, monthEndDate];
    return re_arr;
  }
  //列表日期时间格式化
  public dateFormat(row: any, column: any, cellValue: any) {
    //    let aa = new Date(cellValue).toUTCString();
    let XXXXTime = Date.parse(cellValue);
    //console.log(XXXXTime);
    let dayNames: any[] = [
      "周一",
      "周二",
      "周三",
      "周四",
      "周五",
      "周六",
      "周日"
    ];
    return cellValue
      ? fecha.format(new Date(XXXXTime - 8 * 3600 * 1000), "yyyy-MM-dd") +
          " (" +
          dayNames[new Date(XXXXTime - 8 * 3600 * 1000).getUTCDay()] +
          ")"
      : "";
  }
  public numberFormat(row: any, column: any, cellValue: any) {
    return cellValue.toLocaleString();
  }
}
</script>

<style lang="scss">
@import "@/assets/scss/style.scss";
/* @import url(); 引入css类 */
.el-table {
  .success-row {
    background: green;
  }
  th {
    padding: 3px;
    text-align: center;
  }
  td {
    padding: 0px;
    text-align: right;
  }
  * {
    font-size: 0.8rem;
  }
}
</style>
