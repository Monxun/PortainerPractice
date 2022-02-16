import {NgModule} from '@angular/core';
import {DashboardComponent} from './dashboard.component';
import {DashboardNavComponent} from './dashboard-nav/dashboard-nav.component';
import {DashboardRoutingModule} from '@dashboard/dashboard-routing.module';
import {AccountsDashboardComponent} from './accounts-dashboard/accounts-dashboard.component';
import {SummaryComponent} from './summary/summary.component';
import {LogoModule} from '@app/logo/logo.module';
import {AppIconsModule} from '@app/app-icons.module';
import {TabNavComponent} from './dashboard-nav/tab-nav/tab-nav.component';
import {NavTabComponent} from '@dashboard/dashboard-nav/tab-nav/nav-tab.component';
import {UserAvatarComponent} from './user-avatar/user-avatar.component';
import {DrawerComponent} from './dashboard-nav/drawer/drawer.component';
import {NgbButtonsModule, NgbPaginationModule, NgbTooltipModule} from '@ng-bootstrap/ng-bootstrap';
import {AccountViewComponent} from './account-view/account-view.component';
import {AccountLabelPipe} from './pipes/account-label.pipe';
import {AccountPageComponent} from './account-page/account-page.component';
import {CommonModule} from '@angular/common';
import {TransactionsViewComponent} from './transactions-view/transactions-view.component';
import {TransactionAmountPipe} from './pipes/transaction-amount.pipe';
import {TransactionEnumPipe} from './pipes/transaction-enum.pipe';
import {TransactionDescriptionPipe} from './pipes/transaction-description.pipe';
import {SortToggleComponent} from './transactions-view/sort-toggle/sort-toggle.component';
import {FormsModule} from '@angular/forms';
import {TransactionRowComponent} from './transactions-view/transaction-row/transaction-row.component';
import {TransactionsTableComponent} from './transactions-view/transactions-table/transactions-table.component';
import {SearchTransactionsComponent} from './transactions-view/search-transactions/search-transactions.component';
import {TransferFundsViewComponent} from './transfer-funds-view/transfer-funds-view.component';
import {AppMaskModule} from '@app/app-mask.module';
import {AppCurrencyMaskModule} from '@app/app-currency-mask.module';
import {TransferFundsPageComponent} from './transfer-funds-page/transfer-funds-page.component';
import {BreakpointDetectorComponent} from '@dashboard/breakpoint-detector/breakpoint-detector.component';

@NgModule({
  declarations: [
    DashboardComponent,
    DashboardNavComponent,
    AccountsDashboardComponent,
    SummaryComponent,
    TabNavComponent,
    NavTabComponent,
    UserAvatarComponent,
    DrawerComponent,
    AccountViewComponent,
    AccountLabelPipe,
    AccountPageComponent,
    TransactionsViewComponent,
    TransactionAmountPipe,
    TransactionEnumPipe,
    TransactionDescriptionPipe,
    SortToggleComponent,
    TransactionRowComponent,
    TransactionsTableComponent,
    SearchTransactionsComponent,
    TransferFundsViewComponent,
    TransferFundsPageComponent,
    BreakpointDetectorComponent
  ],
  imports: [
    CommonModule,
    DashboardRoutingModule,
    LogoModule,
    AppIconsModule,
    NgbTooltipModule,
    NgbPaginationModule,
    NgbButtonsModule,
    FormsModule,
    AppMaskModule,
    AppCurrencyMaskModule
  ]
})
export class DashboardModule {}
