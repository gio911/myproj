import { AfterViewInit, Component, ElementRef, OnInit } from '@angular/core';
import { CurrentPaymentsService } from '../shared/services/current-payments.service';
import {MatDialog, MAT_DIALOG_DATA, MatDialogConfig} from '@angular/material/dialog'
import { AddCurrentPaymentsDialogComponent } from '../add-current-payments-dialog/add-current-payments-dialog.component';
import {ViewChild} from '@angular/core';
import {MatPaginator} from '@angular/material/paginator';
import {MatSort} from '@angular/material/sort';
import {MatTableDataSource, MatTableModule} from '@angular/material/table';

import { ToastrService } from 'ngx-toastr';
import { Payment } from '../shared/interfaces';
import { DomSanitizer, SafeUrl } from '@angular/platform-browser';
import { WordDialogComponent } from '../word-dialog/word-dialog.component';
import {NgbModal} from '@ng-bootstrap/ng-bootstrap'
@Component({
  selector: 'app-current-payments-page',
  templateUrl: './current-payments-page.component.html',
  styleUrls: ['./current-payments-page.component.css']
})
export class CurrentPaymentsPageComponent implements OnInit{
  
  displayedColumns: string[] = ['counterparty', 
                                'contract', 
                                'date', 
                                'num', 
                                'sum', 
                                'comment', 
                                'edit', 
                                'delete', 
                                'create', 
                                'show',
                                'send'
                              ];
  dataSource: MatTableDataSource<any>;
  pdfUrl:any=''

  @ViewChild(MatPaginator) paginator: MatPaginator;
  @ViewChild(MatSort) sort: MatSort;
  pdfDocument:any
  pdfData: any;
  constructor(private dialog:MatDialog, 
              private currentPaymentService:CurrentPaymentsService,
              private toaster:ToastrService,
              ){
    
  }
  selectedCheckboxes:[]=[]

  ngOnInit(): void {
    this.getAllPayments()
  }

  getAllPayments(){
    this.currentPaymentService.fetchPayments()
      .subscribe({
        next:(res)=>{
          console.log(res, 543);

          this.dataSource = new MatTableDataSource(res)
          this.dataSource.paginator = this.paginator
          this.dataSource.sort = this.sort
        }
      })
  }

  openDialog() {
    this.dialog.open(AddCurrentPaymentsDialogComponent, {
        width:'30%'      
    }).afterClosed().subscribe(val=>{
      if(val==='save'){
        this.getAllPayments()
      }
    })
    
  }

  confirmDelete() {
    const shouldDelete = window.confirm('Are you sure you want to delete this item?');
    if (shouldDelete) {
      return true
    } else {
      return false
    }
  }

  applyFilter(event: Event) {
    const filterValue = (event.target as HTMLInputElement).value;
    this.dataSource.filter = filterValue.trim().toLowerCase();

    if (this.dataSource.paginator) {
      this.dataSource.paginator.firstPage();
    }
  }

  editPayment(row:any){
    this.dialog.open(AddCurrentPaymentsDialogComponent, {
      width:'30%',
      data: row
    }
   ).afterClosed().subscribe(res=>{
    if(res==='update'){
      this.getAllPayments()
    }
   })
  }

  deletePayment(id:number){
    const state = this.confirmDelete()

    if(state){
      this.currentPaymentService.deleteProduct(id)
        .subscribe({
          next:()=>{
            this.toaster.success('Платеж удален')
            this.getAllPayments()
          },
          error:()=>{
            this.toaster.error('Ошибка при удалении')  
        }})
    }
   }

   createPdf(id:number, payment:Payment){
    console.log(payment, 84848);
    
      this.currentPaymentService.createPdfFile(id, payment)
        .subscribe({
          next:(res)=>{
            console.log(res);
            this.getAllPayments()
          },
          error:(err)=>{
            console.log('err',err);
            
          }
        })
        
   }

  pdf(id:number, payment:Payment){
    this.currentPaymentService.fetchPdf(id,payment)
    .subscribe({
      next:(res)=>{
        console.log(res);
        this.pdfData = res;

        let blob:Blob = res.body as Blob
        let url = window.URL.createObjectURL(blob)
        this.pdfUrl = url
        const dialogConfig = new MatDialogConfig();
        dialogConfig.width = '1000px';   // Set the width
        dialogConfig.height = '1000px'
        dialogConfig.data = { pdfUrl: this.pdfUrl};

        this.dialog.open(WordDialogComponent, dialogConfig)
      },
      error:(err)=>{
        console.log('err',err);
        
      }
    })
  }

  sendDoc(id:number, payment:Payment){
    this.currentPaymentService.sendEmail(id, payment).subscribe({
      next:(res)=>{
        console.log(res, 9494)
      },
      error:()=>{

      }
    })
  }

  toggleCheckbox(id:number){

  }

}



