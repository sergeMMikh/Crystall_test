// import {Link} from "react-router-dom";
import PageContainer from '../../components/page.container/Page.container';
import Button from '../../components/button/Button';
import styles from './Create.schedule.page.module.scss';
import { Datepicker } from '../../components/datepicker/Datepicker';
import ChooseButton from '../../components/button/Choose.button';

export default function CreateShedulePage() {
	return (
		<>
			<PageContainer.Header title="Составить расписание тренеров" />
			<PageContainer.Body>
				<Datepicker />
				<div className={styles['btns-wrap']}>
					<ChooseButton
						title={'Выберите тренера'}
						downArrow={'calendar_arrow_down.svg'}
						className={styles.btn}
					/>
					<ChooseButton
						title={'Выберите площадку'}
						downArrow={'calendar_arrow_down.svg'}
						className={styles.btn}
					/>
					<Button>Отправить расписание</Button>
				</div>
			</PageContainer.Body>
		</>
	);
}
