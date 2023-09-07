import { Component, OnInit, ViewChild } from '@angular/core';
import { MatDialog, MatDialogConfig } from '@angular/material/dialog';
import { MatPaginator } from '@angular/material/paginator';
import { MatSort } from '@angular/material/sort';
import { MatTableDataSource } from '@angular/material/table';
import { CurrentPaymentsService } from '../shared/services/current-payments.service';
import { ToastrService } from 'ngx-toastr';
import { Payment } from '../shared/interfaces';
import { ArchivePaymentsService } from '../shared/services/archive-payment.service';
import { WordDialogComponent } from '../word-dialog/word-dialog.component';
import { CommentmentsDialodComponent } from '../commentments-dialog/commentments-dialog.component';

@Component({
  selector: 'app-archive-payments-page',
  templateUrl: './archive-payments-page.component.html',
  styleUrls: ['./archive-payments-page.component.css']
})
export class ArchivePageComponent implements OnInit {

  displayedColumns: string[] = [
                                'counterparty', 
                                'contract', 
                                'date', 
                                'num', 
                                'sum', 
                                'comment',
                                'backup', 
                                'delete', 
                                'show',
                                'description'
                              ];
  dataSource: MatTableDataSource<any>;
  pdfUrl:any=''

  @ViewChild(MatPaginator) paginator: MatPaginator;
  @ViewChild(MatSort) sort: MatSort;
  pdfDocument:any
  pdfData: any;
  constructor(private dialog:MatDialog, 
              private archivePaymentService:ArchivePaymentsService, 
              private toaster:ToastrService,
              ){
    
  }
  selectedCheckboxes:[]=[]


  confirmDelete(text:string) {
    const shouldDelete = window.confirm(text);
    if (shouldDelete) {
      return true
    } else {
      return false
    }
  }


  ngOnInit(): void {
      this.getAllArchivePayments()
  }

  deletePayment(id:number){
    const state = this.confirmDelete('Удалить платеж ?')
    if(state){
      this.archivePaymentService.deletePayment(id).subscribe({
        next:(res)=>{
          this.getAllArchivePayments()
          this.toaster.success(res)
          
        },
        error:(err)=>{
          console.log(err);
          
        }
      })
    }
 
  }

  pdf(id:number, payment:Payment){
    console.log('rewewrw');
    
      this.archivePaymentService.fetchPdf(id, payment).subscribe({
        next:(res)=>{
          console.log(5858585849949494);
          
        this.pdfData = res;

        let blob:Blob = res.body as Blob
        let url = window.URL.createObjectURL(blob)
        this.pdfUrl = url
        const dialogConfig = new MatDialogConfig();
        dialogConfig.width = '1000px'
        dialogConfig.height = '1000px'
        dialogConfig.data = { pdfUrl: this.pdfUrl};

        this.dialog.open(WordDialogComponent, dialogConfig)
        },
        error:()=>{

        }
      })
  }

  getAllArchivePayments(){
    this.archivePaymentService.getAllArchivePayments().subscribe({
      next:(payments)=>{
        console.log(payments, 'ARCHIVE')

        this.dataSource = new MatTableDataSource(payments)
        this.dataSource.paginator = this.paginator
        this.dataSource.sort = this.sort
      },
      error:()=>{

      }
    })
  }


  applyFilter(event: Event) {
    const filterValue = (event.target as HTMLInputElement).value;
    this.dataSource.filter = filterValue.trim().toLowerCase();

    if (this.dataSource.paginator) {
      this.dataSource.paginator.firstPage();
    }
  }

  backToCurrentPayments(id:number){

    this.archivePaymentService.backPayment(id).subscribe({
      next:(res)=>{
        
        this.toaster.success(res)
        this.getAllArchivePayments()

      },
      error:()=>{

      }
    })

  }

  showToDoList(payment:Payment){
      this.dialog.open(CommentmentsDialodComponent,{
        width:'200%',
        height:'300%',
        data:{
          payment:payment
        }
      })
  }

}
