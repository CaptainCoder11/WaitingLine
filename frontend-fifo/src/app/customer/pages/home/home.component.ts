import { Component, OnInit } from '@angular/core';
import { DialogRef, DialogService } from '@progress/kendo-angular-dialog';
import { NgxSpinnerService } from 'ngx-spinner';
import { CustomerWaiting } from 'src/app/common/models/customer-waiting.model';
import { Store } from 'src/app/common/models/store.model';
import { AuthenticationService } from 'src/app/common/services/authentication.service';
import { StoreService } from 'src/app/common/services/store.service';
import { WaitingListFirebaseService } from 'src/app/common/services/waiting-list.firebase.service';
import { DISPLAY_LOGO } from 'src/app/common/utils/functions';
import { NotyUtil } from 'src/app/common/utils/noty-util';
import { CustomerStoreDetailsComponent } from '../../components/store-details/store-details.component';

@Component({
  selector: 'app-customer-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css'],
})
export class CustomerHomeComponent implements OnInit {
  DISPLAY_LOGO = DISPLAY_LOGO;

  stores: Store[];
  masterStoreList: Store[];
  customerWaiting: CustomerWaiting;
  searchStore: string;

  constructor(
    private storeService: StoreService,
    private waitingListFirebaseService: WaitingListFirebaseService,
    private spinner: NgxSpinnerService,
    public authService: AuthenticationService,
    private dialogService: DialogService
  ) {}

  ngOnInit(): void {
    this.spinner.show();
    this.storeService.getAll().subscribe(
      (stores) => {
        this.spinner.hide();
        this.masterStoreList = stores;
        this.stores = stores;
      },
      (error) => this.spinner.hide()
    );

    this.waitingListFirebaseService.get().subscribe((waitingList) => {
      this.customerWaiting = waitingList.find(
        (x) => x.id == this.authService.getCustomer?.id
      );
    });
  }

  showStoreDetails(model) {
    const dialog: DialogRef = this.dialogService.open({
      content: CustomerStoreDetailsComponent,
      width: 500,
    });
    const inputData = dialog.content.instance;
    inputData.store = model;
    inputData.customerWaiting = this.customerWaiting;

    dialog.result.subscribe();
  }

  onSearch(event) {
    const val: string = event.target.value;

    if (!val) {
      this.stores = this.masterStoreList;
    } else {
      this.stores = this.masterStoreList.filter((x) =>
        x.name.toLowerCase().includes(val.toLocaleLowerCase())
      );
    }
  }

  removeFromWaitingLine(storeId) {
    const userId = this.authService.getCustomer.id;
    this.spinner.show();
    this.storeService.removeWaitingLine(userId, storeId).subscribe(
      () => {
        this.spinner.hide();
        NotyUtil.success('You have been removed from waiting line!');
      },
      (e) => {
        this.spinner.hide();
        const error = e.error.message || e.error.error;
        NotyUtil.error(error);
      },
      () => {
        this.spinner.hide();
      }
    );
  }
}
