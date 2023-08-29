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
  
  displayedColumns: string[] = ['counterparty', 'contract', 'date', 'num', 'sum', 'comment', 'edit', 'delete', 'createPdf', 'show', ];
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

  // ngAfterViewInit(): void {
  //   const container = this.pdfViewer.nativeElement
  //   const url = this.pdfDocument

  //   pdfjsLib.getDocument(url).promise.then((pdfDoc:any)=>{
  //     this.pdfDocument=pdfDoc
  //     //this.renderPdf()

  //   })
  // }

  // renderPdf(){
  //   const container = this.pdfViewer.nativeElement
  //   for (let pageNum=1; pageNum<=this.pdfDocument.numPages; pageNum++){
  //     this.pdfDocument.getPage(pageNum).then((page:any)=>{
  //       const canvas = document.createElement('canvas')
  //       const context = canvas.getContext('2d')
  //       canvas.style.display='block'
  //       container.appendChild(canvas)
  //       canvas.height = 400
  //       const viewport = page.getViewport({scale:1})
  //       canvas.width = viewport.width

  //       page.render({canvasContext:context, viewport:viewport})
  //     })
  //   }
  // }

  getAllPayments(){
    this.currentPaymentService.fetchPayments()
      .subscribe({
        next:(res)=>{
          console.log(res, 543);
          // const documentData = new Uint8Array(atob(res[0].document).split('').map(char => char.charCodeAt(0)));
          // console.log(documentData);
          
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
          //   this.dialog.open(WordDialogComponent, {
          //     width:'3000%' ,
          //     data:res     
          // })
          //   console.log(res, 94949494)
            //this.pdfObject=res
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
        // this.modalservice.open(this.popupview,{
        //   size:'lg'
        // })
      //   this.dialog.open(WordDialogComponent, {
      //     width:'3000%' ,
      //     data:res     
      // })
      //   console.log(res, 94949494)
        //this.pdfObject=res
        this.dialog.open(WordDialogComponent, dialogConfig)
      },
      error:(err)=>{
        console.log('err',err);
        
      }
    })


 
    
  }
  // displayPdf(): void {
  //   const file = new Blob([this.pdfData], { type: 'application/pdf' });
  //   const pdfUrl = URL.createObjectURL(file);
  //   console.log(pdfUrl, 84848);
    
  //   this.pdfUrl = pdfUrl
  //   // Use this URL in your PDF viewer component
  // }
  toggleCheckbox(id:number){

  }

}



