export * from './login.service';
import { LoginService } from './login.service';
export * from './messenger.service';
import { MessengerService } from './messenger.service';
export const APIS = [LoginService, MessengerService];
